package com.ssafy.happyhouse.interceptor;

import com.ssafy.happyhouse.service.JwtService;
import io.jsonwebtoken.ExpiredJwtException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;

@Component
public class JwtInterceptor implements HandlerInterceptor {

    @Autowired
    private JwtService jwtService;

    public static final Logger logger = LoggerFactory.getLogger(JwtInterceptor.class);

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        logger.info(request.getMethod() + " : " + request.getServletPath());

        // option 요청은 바로 통과시켜주자.
        if (request.getMethod().equals("OPTIONS")) {
            return true;
        } else {
            // request의 parameter에서 auth_token으로 넘어온 녀석을 찾아본다.
            // String token = request.getParameter("auth_token");
            String token = request.getHeader("Authorization");
            if (token != null && token.length() > 0) {
                try {
                    // 유효한 토큰이면 진행, 그렇지 않으면 예외를 발생시킨다.
                    jwtService.checkValid(token);

                    Map<String, Object> check = jwtService.getToken(token);
                    String type = (String)check.get("sub");

                    if (type.equals("acc_token")) {
                        // Access Token 사용 가능 ( 통과)
                        logger.info("Access Token 사용 가능 : {}", token);
                        String rtoken = (String) check.get("RefreshToken");
                        jwtService.checkValid(rtoken);
                        return true;
                    }
                    else if (type.equals("ref_token")) {
                        logger.info("Access Token 갱신 요청 : {}", token);
                        // Refresh Token 으로 재요청
                        try {
                            logger.info("RefreshToken 사용 가능 : {}", token);

                            String atoken = jwtService.createAccessToken(token);
                            logger.info("Access Token 재생성 : {}", atoken);
                            response.getWriter().write(writeResult(atoken));
                            return false;

                        } catch (Exception e) {
                            // 그외의 에러
                            logger.warn("JWT 에러 : {}", e.getMessage());
                            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
                            response.getWriter().write(writeResult("fail"));
                            return false;
                        }
                    }
                    else {
                        // 뭔지 모르는 토큰
                        logger.warn("등록되지 않은 토큰");
                        response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
                        response.getWriter().write(writeResult("fail"));
                        return false;
                    }
                } catch(ExpiredJwtException e) {
                    // Token 만료
                    logger.warn("Token 만료 : {}", e.getMessage());
                    response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
                    response.getWriter().write(writeResult("token"));
                    return false;
                } catch (Exception e) {
                    // 그외의 에러
                    logger.warn("JWT 에러 : {}", e.getMessage());
                    response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
                    response.getWriter().write(writeResult("fail"));
                    return false;
                }
            }
        }

        logger.warn("Token 없음");
        response.setStatus(HttpServletResponse.SC_CONFLICT);
        response.getWriter().write(writeResult("fail"));
        return false;
    }

    public String writeResult (String type) {
        String s = "{\"token\": \"";
        if (type.equals("fail") || type.equals("token")) {
            s += type;
        }
        else {
            s += type;
        }
        s += "\"}";
        return s;
    }
}
