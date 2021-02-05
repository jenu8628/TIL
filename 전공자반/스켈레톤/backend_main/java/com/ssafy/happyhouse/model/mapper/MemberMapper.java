package com.ssafy.happyhouse.model.mapper;

import com.ssafy.happyhouse.model.dto.MemberDto;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface MemberMapper {

    // 로그인 시도
    public MemberDto selectWithIdAndPw(String user_id, String user_password);

    // 회원가입
    public int insertMember(MemberDto dto);

    // 아이디 중복 확인
    public int selectCheckId(String user_id);

    // 회원정보 수정(패스워드)
    public int updateMemberPassword(MemberDto dto);

    // 회원정보 수정(이메일)
    public int updateMemberEmail(MemberDto dto);

    // 회원정보 가져오기(서버전용)
    public MemberDto selectMember(String user_id);
}
