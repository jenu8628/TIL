package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.NoticeDto;
import com.ssafy.happyhouse.model.dto.PageDto;

public interface NoticeService {

    // 한 페이지
    public PageDto makePage(int curPage, String name);

    // 글쓰기
    public void insertNotice(NoticeDto dto);

    // 글삭제
    public boolean deleteNotice(int num);

    // 글수정
    public boolean updateNotice(NoticeDto dto);

    // 글 조회
    public NoticeDto selectNotice(int num);

    // 글검색
//    public PageDto makeSearchPage(int curPage, String name);
}
