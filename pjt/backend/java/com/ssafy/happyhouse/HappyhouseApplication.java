package com.ssafy.happyhouse;

import com.ssafy.happyhouse.interceptor.JwtInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.Arrays;

@SpringBootApplication
public class HappyhouseApplication implements WebMvcConfigurer {

    public static void main(String[] args) {
        SpringApplication.run(HappyhouseApplication.class, args);
    }

    @Autowired
    private JwtInterceptor jwtInterceptor;

    // JWTInterceptor를 설치한다.
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(jwtInterceptor).addPathPatterns("/api/**") // 기본 적용 경로
                .excludePathPatterns(Arrays.asList("/api/login/**", "/api/login", "/api/notice/**",
                        "/api/notice", "/api/board", "/api/board/**", "/api/comment", "/api/comment/**",
                        "/api/house/**"));// 적용 제외 경로
    }

    // Interceptor를 이용해서 처리하므로 전역의 Corss Origin 처리를 해준다.
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("*")
                .allowedMethods("*")
                .allowedHeaders("*")
                .exposedHeaders("Authorization");
    }

}
