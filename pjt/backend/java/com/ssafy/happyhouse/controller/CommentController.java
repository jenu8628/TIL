package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.CommentDto;
import com.ssafy.happyhouse.service.CommentService;
import com.ssafy.happyhouse.service.JwtService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/comment")
public class CommentController {

    @Autowired
    private CommentService commentService;

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(CommentController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    @GetMapping(value = "{no}", produces = "application/json; charset=utf8")
    public ResponseEntity<List<CommentDto>> getComment(@PathVariable("no") int num) {
        List<CommentDto> commentList = commentService.selectComment(num);
        logger.info("getComment - 댓글 요청 : {} ", num);
        return new ResponseEntity<>(commentList, HttpStatus.OK);
    }

    @PostMapping(value = "")
    public ResponseEntity<String> postComment(@RequestBody Map<String, String> map, HttpServletRequest request) {
        CommentDto dto = new CommentDto();
        dto.setBoard_num(Integer.parseInt(map.get("board_num")));
        dto.setComment_content(map.get("comment_content"));
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            dto.setComment_writer(id);
            System.out.println(dto);
            logger.info("postComment - 게시판 댓글 작성 : {}", dto);
            commentService.insertComment(dto);
            return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
        } catch (IllegalArgumentException e) {
            logger.warn("postComment - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("postComment - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping(value = "{no}")
    public ResponseEntity<String> putComment(@PathVariable("no") int num, @RequestBody CommentDto dto,
                                             HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            dto.setBoard_num(num);
            dto.setComment_writer(id);
            if (commentService.updateComment(dto)) {
                logger.info("putComment - 댓글 수정 : {}", dto);
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            } else {
                logger.warn("putComment - 댓글 수정 실패 : {}", id);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }
        } catch (IllegalArgumentException e) {
            logger.warn("putComment - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("putComment - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping(value = "{no}")
    public ResponseEntity<String> deleteComment(@PathVariable("no") int num, HttpServletRequest request) {
        String token = request.getHeader("Authorization");
        try {
            String atoken = (String)jwtService.getToken(token).get("RefreshToken");
            String id = (String) ((Map)jwtService.getToken(atoken).get("UserInfo")).get("user_id");
            if (commentService.deleteComment(num, id)) {
                logger.info("deleteComment - 댓글 삭제 : {}", num);
                return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
            } else {
                logger.warn("deleteComment - 댓글 삭제 실패 : {}", id);
                return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
            }

        } catch (IllegalArgumentException e) {
            logger.warn("deleteComment - 비로그인 접근 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            logger.warn("deleteComment - 에러 : {}", e.getMessage());
            return new ResponseEntity<>(FAIL, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
