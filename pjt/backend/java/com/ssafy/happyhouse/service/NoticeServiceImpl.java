package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.NoticeDto;
import com.ssafy.happyhouse.model.dto.PageDto;
import com.ssafy.happyhouse.model.mapper.NoticeMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NoticeServiceImpl implements NoticeService {

    @Autowired
    private SqlSession sqlSession;
    // 한 페이지에 보여질 갯수
    private static final int COUNT_PER_PAGE = 10;

    @Override
    public PageDto makePage(int curPage, String name) {
        int totalCnt = sqlSession.getMapper(NoticeMapper.class).selectTotalCount(name);
        int totalPageCnt = totalCnt/COUNT_PER_PAGE;
        if (totalCnt % COUNT_PER_PAGE > 0) totalPageCnt++;

        int startPage = (curPage-1) / 10 * 10 + 1;
        int endPage = startPage + 9;

        if (totalPageCnt < endPage) endPage = totalPageCnt;

        int startRow = (curPage - 1 ) * 10;

        List<NoticeDto> noticeList = sqlSession.getMapper(NoticeMapper.class).selectPage(startRow, COUNT_PER_PAGE, name);

        return new PageDto(noticeList, curPage, startPage, endPage, totalPageCnt);
    }

    @Override
    public void insertNotice(NoticeDto dto) {
        sqlSession.getMapper(NoticeMapper.class).insertNotice(dto);
    }

    @Override
    public boolean deleteNotice(int num) {
        return sqlSession.getMapper(NoticeMapper.class).deleteNotice(num) != 0;
    }

    @Override
    public boolean updateNotice(NoticeDto dto) {
        return sqlSession.getMapper(NoticeMapper.class).updateNotice(dto) != 0;
    }

    @Override
    public NoticeDto selectNotice(int num) {
        sqlSession.getMapper(NoticeMapper.class).updateCnt(num);
        return sqlSession.getMapper(NoticeMapper.class).selectNotice(num);
    }

//    @Override
//    public PageDto makeSearchPage(int curPage, String name) {
//        int totalCnt = sqlSession.getMapper(NoticeMapper.class).selectSearchAllPage(name);
//        int totalPageCnt = totalCnt/COUNT_PER_PAGE;
//        if (totalCnt % COUNT_PER_PAGE > 0) totalPageCnt++;
//
//        int startPage = (curPage-1) / 10 * 10 + 1;
//        int endPage = startPage + 9;
//
//        if (totalPageCnt < endPage) endPage = totalPageCnt;
//
//        int startRow = (curPage - 1) * 10;
//
//        List<NoticeDto> noticeList = sqlSession.getMapper(NoticeMapper.class).selectSearchPage(startRow, COUNT_PER_PAGE, name);
//
//        return new PageDto(noticeList, curPage, startPage, endPage, totalPageCnt);
//    }
}
