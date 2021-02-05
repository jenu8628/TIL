package com.ssafy.happyhouse.model.mapper;

import com.ssafy.happyhouse.model.dto.CommentDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface CommentMapper {

    // 하나의 게시글 댓글 갖고오기
    public List<CommentDto> selectComment(int num);

    // 댓글 쓰기
    public void insertComment(CommentDto dto);

    // 댓글 수정
    public int updateComment(CommentDto dto);

    // 댓글 삭제
    public int deleteComment(@Param("num") int num, @Param("id") String id);

    // 게시글 삭제 시 댓글 전체 삭제
    public void deleteAllComment(int num);
}
