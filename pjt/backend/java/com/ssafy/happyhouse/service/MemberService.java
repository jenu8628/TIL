package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.MemberDto;

public interface MemberService {

    // 로그인 시도
    public MemberDto selectWithIdAndPw(MemberDto dto);

    // 회원 가입
    public boolean insertMember(MemberDto dto);

    // 아이디 중복 확인
    public boolean selectCheckId(String id);

    // 회원 정보 수정
    public boolean updateMember(MemberDto dto);

    // 회원 정보 가져오기
    public MemberDto selectMember(String user_id);
}
