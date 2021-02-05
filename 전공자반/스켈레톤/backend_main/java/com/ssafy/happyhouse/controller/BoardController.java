package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.BoardDto;
import com.ssafy.happyhouse.model.dto.PageDto;
import com.ssafy.happyhouse.service.BoardService;
import com.ssafy.happyhouse.service.JwtService;
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
@RequestMapping("/api/board")
public class BoardController {

    @Autowired
    private BoardService boardService;

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(BoardController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    @GetMapping(value = "list", produces = "application/json; charset=utf8")
    public ResponseEntity<PageDto> getNoticeList(@RequestParam(value = "name") String name, @RequestParam(value = "page")int page) {
        PageDto pageDto = null;
        if (page > 0) {
            pageDto = boardService.makePage(page, name);
        }
        logger.info("getNoticeList - 공지사항 페이징 요청 : {}", pageDto);
        return new ResponseEntity<>(pageDto, HttpStatus.OK);
    }

    @GetMapping(value = "{no}", produces = "application/json; charset=utf8")
    public ResponseEntity<BoardDto> getBoard(@PathVariable("no") int num) {
        BoardDto boardDto = boardService.selectBoard(num);
        logger.info("getBoard - 게시판 게시글 요청 : {}", boardDto);
        if (boardDto == null) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(boardDto, HttpStatus.OK);
        }
    }

    @PostMapping(value = "")
    public ResponseEntity<String> postBoard(@RequestBody BoardDto dto, HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            dto.setBoard_writer(id);
            logger.info("postBoard - 게시판 게시글 작성 : {}", dto);
            boardService.insertBoard(dto);
            return new ResponseEntity<>(SUCCESS, HttpStatus.OK);

        } catch (IllegalArgumentException e) {
            logger.warn("postBoard - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("postBoard - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping(value = "{no}")
    public ResponseEntity<String> putBoard(@PathVariable("no") int num, @RequestBody BoardDto dto,
                                           HttpServletRequest request) {
        dto.setBoard_num(num);
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            if (!id.equals(boardService.selectBoard(num).getBoard_writer())) {
                logger.info("putBoard - 다른 사용자 접근 : {}", id);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
            logger.info("putBoard - 게시판 게시글 수정 : {}", dto);
            if (boardService.updateBoard(dto)) {
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (IllegalArgumentException e) {
            logger.warn("putBoard - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("putBoard - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping(value = "{no}")
    public ResponseEntity<String> deleteBoard(@PathVariable("no") int num, HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            int info = (Integer) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_info");
            if (!id.equals(boardService.selectBoard(num).getBoard_writer()) || info == 1) {
                logger.info("deleteBoard - 다른 사용자 접근 : {}", id);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
            logger.info("deleteBoard - 게시판 게시글 삭제 : {}", num);
            if (boardService.deleteBoard(num)) {
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (IllegalArgumentException e) {
            logger.warn("deleteBoard - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("deleteBoard - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
