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

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/user")
public class MemberController {

    @Autowired
    private MemberService memberService;

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    // 토큰용
    @GetMapping("/token")
    public void getToken() {
        logger.error("getToken - 토큰용");
        return;
    }

    // 개인 정보 불러오기
    @GetMapping("/info")
    public ResponseEntity<Map<String, Object>> getMember (HttpServletRequest request) {
        Map<String, Object> resultMap = new HashMap<>();
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            resultMap.put("UserInfo", jwtService.getToken(atoken).get("UserInfo"));
//            resultMap.put("message", "Info Success");
            logger.info("getMember - 개인 정보 요청 : {}", resultMap.get("UserInfo"));
            return new ResponseEntity<>(resultMap, HttpStatus.OK);
        } catch (Exception e) {
            logger.error("getMember - 정보조회 실패 : {}", e.getMessage());
//                resultMap.put("message", e.getMessage());
//            resultMap.put("message", "Info Fail");
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }
    }


    // 개인 정보 수정
    @PutMapping("/modify")
    public ResponseEntity<String> putModify (@RequestBody MemberDto dto, HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        String id;
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
        } catch (Exception e) {
            logger.error("putModify - 정보조회 실패 : {}", e.getMessage());
//            resultMap.put("result", "false");
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
        if (id != null && id.length() > 0) {
            dto.setUser_id(id);
            if (memberService.updateMember(dto)) {
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            }
        }
        return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
    }
}
