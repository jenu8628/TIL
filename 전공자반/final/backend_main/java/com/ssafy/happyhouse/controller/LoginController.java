package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.MemberDto;
import com.ssafy.happyhouse.service.JwtService;
import com.ssafy.happyhouse.service.MemberService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/login")
public class LoginController {

    @Autowired
    private MemberService memberService;

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(LoginController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    // 로그인
    @PostMapping("")
    public ResponseEntity<Map<String, Object>> postLogin(@RequestBody MemberDto dto, HttpServletResponse response) {
        Map<String, Object> resultMap = new HashMap<>();
        MemberDto loginUser = memberService.selectWithIdAndPw(dto);
        try {
            if (loginUser != null) {
//				jwt.io에서 확인
//				로그인 성공했다면 토큰을 생성한다.
                String rtoken = jwtService.createRefreshToken(loginUser);
                logger.trace("postLogin - RefreshToken 토큰정보 : {}", rtoken);

                String atoken = jwtService.createAccessToken(rtoken);
                logger.trace("postLogin - AccessToken 토큰정보 ㅣ {}", atoken);

                // 비밀번호 제거 후 전송
                loginUser.setUser_password("");
                resultMap.put("ref_token", rtoken);
                resultMap.put("acc_token", atoken);
                resultMap.put("UserInfo", loginUser);
                return new ResponseEntity<>(resultMap, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(resultMap, HttpStatus.NO_CONTENT);
            }
        } catch (Exception e) {
            logger.error("postLogin = 로그인 실패 : {}", e);
            return new ResponseEntity<>(resultMap, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // 회원가입
    @PostMapping("/signup")
    public ResponseEntity<String> postSginup (@RequestBody MemberDto dto) {
        logger.info("postSginup = 회원가입 : {}", dto);
        if (memberService.insertMember(dto)) {
            return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        }
    }

    // 아이디 중복 확인
    @PostMapping("/signup/check")
    public ResponseEntity<String> postCheckId (@RequestBody Map<String, String> map) {
        String id = map.get("user_id");
        logger.info("postCheckId = 아이디 중복 확인 : {}", id);
        if (memberService.selectCheckId(id)) {
            return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        }
    }
}
