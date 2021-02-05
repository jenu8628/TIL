package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.CommentDto;
import com.ssafy.happyhouse.model.mapper.CommentMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CommentServiceImpl implements CommentService {

    @Autowired
    private SqlSession sqlSession;

    @Override
    public List<CommentDto> selectComment(int num) {
        return sqlSession.getMapper(CommentMapper.class).selectComment(num);
    }

    @Override
    public void insertComment(CommentDto dto) {
        sqlSession.getMapper(CommentMapper.class).insertComment(dto);
    }

    @Override
    public boolean updateComment(CommentDto dto) {
        return sqlSession.getMapper(CommentMapper.class).updateComment(dto) != 0;
    }

    @Override
    public boolean deleteComment(int num, String id) {
        return sqlSession.getMapper(CommentMapper.class).deleteComment(num, id) != 0;
    }
}
