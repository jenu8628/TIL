package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.BoardDto;
import com.ssafy.happyhouse.model.dto.PageDto;

public interface BoardService {

    // 한 페이지
    public PageDto makePage(int curPage, String anme);

    // 글쓰기
    public void insertBoard(BoardDto dto);

    // 글삭제
    public boolean deleteBoard(int num);

    // 글수정
    public boolean updateBoard(BoardDto dto);

    // 글 조회
    public BoardDto selectBoard(int num);
}
