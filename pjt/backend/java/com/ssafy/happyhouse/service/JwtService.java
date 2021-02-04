package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.MemberDto;
import io.jsonwebtoken.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.Map;

@Component
public class JwtService {

    public static final Logger logger = LoggerFactory.getLogger(JwtService.class);

    private String Signature = "TOKEN";
    private final Long REF_EXPIRE = 60L * 24 * 10;
    private final Long ACC_EXPIRE = 1L;

    //	로그인 성공시 사용자 정보를 기반으로 JWTToken을 생성하여 반환.
    public String createRefreshToken(MemberDto dto) {
        dto.setUser_password("");
        JwtBuilder jwtBuilder = Jwts.builder();
//		JWT Token = Header + Payload + Signature

//		Header 설정
        jwtBuilder.setHeaderParam("typ", "JWT"); // 토큰의 타입으로 고정 값.

//		Payload 설정
        jwtBuilder
                .setSubject("ref_token") // 토큰의 제목 설정
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * REF_EXPIRE)) // 유효기간 설정
                .claim("UserInfo", dto);//.claim("greeting", "환영합니다. " + memberDto.getUser_id()); // 담고 싶은 정보 설정.

//		signature 설정
        jwtBuilder.signWith(SignatureAlgorithm.HS256, Signature.getBytes());

//		마지막 직렬화 처리
        String jwt = jwtBuilder.compact();
        logger.info("jwt : {}", jwt);
        return jwt;
    }

    public String createAccessToken(String rt) {
        JwtBuilder jwtBuilder = Jwts.builder();
//		JWT Token = Header + Payload + Signature

//		Header 설정
        jwtBuilder.setHeaderParam("typ", "JWT"); // 토큰의 타입으로 고정 값.

//		Payload 설정
        jwtBuilder
                .setSubject("acc_token") // 토큰의 제목 설정
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * ACC_EXPIRE)) // 유효기간 설정
                .claim("RefreshToken", rt);// 담고 싶은 정보 설정.

//		signature 설정
        jwtBuilder.signWith(SignatureAlgorithm.HS256, Signature.getBytes());

//		마지막 직렬화 처리
        String jwt = jwtBuilder.compact();
        logger.info("jwt : {}", jwt);
        return jwt;
    }

    public void checkValid(String jwt) {
        Jwts.parser().setSigningKey(Signature.getBytes()).parseClaimsJws(jwt);
    }

    //	JWT Token을 분석해서 필요한 정보를 반환.
    public Map<String, Object> getToken(String jwt) {
        Jws<Claims> claims = null;
        try {
            claims = Jwts.parser().setSigningKey(Signature.getBytes()).parseClaimsJws(jwt);
        } catch (final Exception e) {
            throw new RuntimeException();
        }

        logger.info("claims : {}", claims);
        // Claims는 Map의 구현체이다.
        return claims.getBody();
    }
}