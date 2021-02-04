package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.house.TestDto;
import com.ssafy.happyhouse.model.mapper.HouseMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TestService {

    @Autowired
    SqlSession sqlSession;

    public List<TestDto> selectCorona() {
        return sqlSession.getMapper(HouseMapper.class).selectTest1();
    }

    public void updateCorona(int clinic_no, String clinic_lat, String clinic_lng) {
        sqlSession.getMapper(HouseMapper.class).updateTest1(clinic_no, clinic_lat, clinic_lng);
    }

    public void updateSubway(int subway_no, String subway_lat, String subway_lng) {
        sqlSession.getMapper(HouseMapper.class).updateTest2(subway_no, subway_lat, subway_lng);
    }

    public List<TestDto> selectSubway() {
        return sqlSession.getMapper(HouseMapper.class).selectTest2();
    }
}
