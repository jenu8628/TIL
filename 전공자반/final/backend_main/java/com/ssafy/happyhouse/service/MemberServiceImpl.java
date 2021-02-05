package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.MemberDto;
import com.ssafy.happyhouse.model.mapper.MemberMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberServiceImpl implements MemberService {

    @Autowired
    SqlSession sqlSession;

    @Override
    public MemberDto selectWithIdAndPw(MemberDto dto) {
        return sqlSession.getMapper(MemberMapper.class).selectWithIdAndPw(dto.getUser_id(), dto.getUser_password());
    }

    @Override
    public boolean insertMember(MemberDto dto) {
        return sqlSession.getMapper(MemberMapper.class).insertMember(dto) == 1;
    }

    @Override
    public boolean selectCheckId(String user_id) {
        return sqlSession.getMapper(MemberMapper.class).selectCheckId(user_id) == 0;
    }

    @Override
    public boolean updateMember(MemberDto dto) {
        boolean result = true;
        if ( dto.getUser_password() != null && dto.getUser_password().length() > 0) {
            result &= sqlSession.getMapper(MemberMapper.class).updateMemberPassword(dto) == 1;
        }
        if ( dto.getUser_email() != null && dto.getUser_email().length() > 0) {
            result &= sqlSession.getMapper(MemberMapper.class).updateMemberEmail(dto) == 1;
        }
        return result;
    }

    @Override
    public MemberDto selectMember(String user_id) {
        return sqlSession.getMapper(MemberMapper.class).selectMember(user_id);
    }
}
