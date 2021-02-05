package com.ssafy.happyhouse.model.mapper;

import com.ssafy.happyhouse.model.dto.NoticeDto;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface NoticeMapper {

    // 전체 게시글 조회
    public int selectTotalCount(String name);

    // 한 페이지에 보여질 게시글
    public List<NoticeDto> selectPage(int startRow, int cnt, String name);

    // 공지사항 등록
    public void insertNotice(NoticeDto dto);

    // 글 삭제
    public int deleteNotice(int num);

    // 글 수정
    public int updateNotice(NoticeDto dto);

    // 글 조회
    public NoticeDto selectNotice(int num);

    // 글 조회수 증가
    public int updateCnt(int num);

    // 검색 결과 총 게시글
//    public int selectSearchAllPage(String name);

    // 검색 결과 한페이지에 보여질 게시글
//    public List<NoticeDto> selectSearchPage(@Param("startRow")int startRow, @Param("cnt")int cnt, @Param("name")String name);
//    public List<NoticeDto> selectSearchPage(int startRow, int cnt, String name);
}
