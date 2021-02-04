package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.CommentDto;

import java.util.List;

public interface CommentService {

    // 게시글 하나에 댓글 가져오기
    public List<CommentDto> selectComment(int num);

    // 댓글 쓰기
    public void insertComment(CommentDto dto);

    // 댓글 수정
    public boolean updateComment(CommentDto dto);

    // 댓글 삭제
    public boolean deleteComment(int num, String id);
}
