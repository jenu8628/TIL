package com.ssafy.happyhouse.model.mapper;

import com.ssafy.happyhouse.model.dto.BoardDto;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BoardMapper {

    // 전체 게시글 조회
    public int selectTotalCount(String name);

    // 한 페이지에 보여질 게시글
    public List<BoardDto> selectPage(int startRow, int cnt, String name);

    // 글 등록
    public void insertBoard(BoardDto dto);

    // 글 삭제
    public int deleteBoard(int num);

    // 글 수정
    public int updateBoard(BoardDto dto);

    // 글 조회
    public BoardDto selectBoard(int num);

    // 글 조회수 증가
    public int updateCnt(int num);
}
