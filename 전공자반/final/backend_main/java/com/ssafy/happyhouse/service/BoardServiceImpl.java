package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.BoardDto;
import com.ssafy.happyhouse.model.dto.PageDto;
import com.ssafy.happyhouse.model.mapper.BoardMapper;
import com.ssafy.happyhouse.model.mapper.CommentMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BoardServiceImpl implements BoardService{

    @Autowired
    private SqlSession sqlSession;
    // 한 페이지에 보여질 갯수
    private static final int COUNT_PER_PAGE = 10;

    @Override
    public PageDto makePage(int curPage, String name) {
        int totalCnt = sqlSession.getMapper(BoardMapper.class).selectTotalCount(name);
        int totalPageCnt = totalCnt/COUNT_PER_PAGE;
        if (totalCnt % COUNT_PER_PAGE > 0) totalPageCnt++;

        int startPage = (curPage-1) / 10 * 10 + 1;
        int endPage = startPage + 9;

        if (totalPageCnt < endPage) endPage = totalPageCnt;

        int startRow = (curPage - 1 ) * 10;

        List<BoardDto> boardList = sqlSession.getMapper(BoardMapper.class).selectPage(startRow, COUNT_PER_PAGE, name);

        return new PageDto(boardList, curPage, startPage, endPage, totalPageCnt);
    }

    @Override
    public void insertBoard(BoardDto dto) {
        sqlSession.getMapper(BoardMapper.class).insertBoard(dto);
    }

    @Override
    public boolean deleteBoard(int num) {
        sqlSession.getMapper(CommentMapper.class).deleteAllComment(num);
        return sqlSession.getMapper(BoardMapper.class).deleteBoard(num) != 0;
    }

    @Override
    public boolean updateBoard(BoardDto dto) {
        return sqlSession.getMapper(BoardMapper.class).updateBoard(dto) != 0;
    }

    @Override
    public BoardDto selectBoard(int num) {
        sqlSession.getMapper(BoardMapper.class).updateCnt(num);
        return sqlSession.getMapper(BoardMapper.class).selectBoard(num);
    }
}
