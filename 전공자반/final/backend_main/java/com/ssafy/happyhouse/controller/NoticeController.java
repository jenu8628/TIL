package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.NoticeDto;
import com.ssafy.happyhouse.model.dto.PageDto;
import com.ssafy.happyhouse.service.JwtService;
import com.ssafy.happyhouse.service.NoticeService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/notice")
public class NoticeController {

    @Autowired
    private NoticeService noticeService;

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(NoticeController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    @GetMapping(value = "list", produces = "application/json; charset=utf8")
    public ResponseEntity<PageDto> getNoticeList(@RequestParam(value = "name") String name, @RequestParam(value = "page")int page) {
        PageDto pageDto = null;
        if (page > 0) {
            pageDto = noticeService.makePage(page, name);
        }
        logger.info("getNoticeList - 공지사항 페이징 요청 : {}", pageDto);
        return new ResponseEntity<>(pageDto, HttpStatus.OK);
    }

//    @GetMapping(value = "search",  produces = "application/json; charset=utf8")
//    public ResponseEntity<PageDto> getSearchNoticeList(@RequestParam(value = "name") String name, @RequestParam(value = "page") int page) {
//        PageDto pageDto = null;
//        if (page > 0) {
//            pageDto = noticeService.makeSearchPage(page, name);
//        }
//        logger.info("getNoticeList - 공지사항 검색 페이징 요청 : {}", pageDto);
//        return new ResponseEntity<>(pageDto, HttpStatus.OK);
//    }

    @GetMapping(value = "{no}", produces = "application/json; charset=utf8")
    public ResponseEntity<NoticeDto> getNotice(@PathVariable("no") int num) {
        NoticeDto noticeDto = noticeService.selectNotice(num);
        logger.info("getNotice - 공지사항 게시글 요청 : {}", noticeDto);
        if (noticeDto == null) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(noticeDto, HttpStatus.OK);
        }
    }

    @PostMapping(value = "")
    public ResponseEntity<String> postNotice(@RequestBody NoticeDto dto, HttpServletRequest request) {
        System.out.println(dto);
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            int info = (Integer)((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_info");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");

            if (info == 1) {
                dto.setNotice_writer(id);
                logger.info("postNotice - 공지사항 게시글 작성 : {}", dto);
                noticeService.insertNotice(dto);
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            } else {
                logger.warn("postNotice - 권한 없는 유저 접근 : {}", dto);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (Exception e) {
            logger.warn("postNotice - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping(value = "{no}")
    public ResponseEntity<String> putNotice(@PathVariable("no") int num, @RequestBody NoticeDto dto, HttpServletRequest request) {
        dto.setNotice_num(num);
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            int info = (Integer)((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_info");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            if (info == 1 && id.equals(noticeService.selectNotice(num).getNotice_writer())) {
                logger.info("putNotice - 공지사항 게시글 수정 : {}", dto);
                if (noticeService.updateNotice(dto)) {
                    return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
                }
            } else {
                logger.warn("putNotice - 권한 없는 유저 접근 : {}", dto);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (Exception e) {
            logger.warn("putNotice - 에러 : {}", dto);
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping(value = "{no}")
    public ResponseEntity<String> deleteNotice(@PathVariable("no") int num, HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            int info = (Integer)((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_info");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");

            if (info == 1 && id.equals(noticeService.selectNotice(num).getNotice_writer())) {
                logger.info("deleteNotice - 공지사항 게시글 삭제 : {}", num);
                if (noticeService.deleteNotice(num)) {
                    return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
                }
            } else {
                logger.warn("deleteNotice - 권한 없는 유저 접근 : {}", num);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (Exception e) {
            logger.warn("deleteNotice - 에러 : {}", num);
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
