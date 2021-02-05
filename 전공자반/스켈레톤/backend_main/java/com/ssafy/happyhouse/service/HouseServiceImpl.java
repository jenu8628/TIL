package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.house.DongDto;
import com.ssafy.happyhouse.model.dto.house.GuDto;
import com.ssafy.happyhouse.model.dto.house.SearchResultDto;
import com.ssafy.happyhouse.model.mapper.HouseMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class HouseServiceImpl implements HouseService {

    @Autowired
    private SqlSession sqlSession;

    @Override
    public List<GuDto> selectGuList() {
        return sqlSession.getMapper(HouseMapper.class).selectGuList();
    }

    @Override
    public List<DongDto> selectDongList(String gu) {
        return sqlSession.getMapper(HouseMapper.class).selectDongList(gu);
    }

    @Override
    public Map<String, Object> selectLatLng(double maxLat, double maxLng, double minLat, double minLng) {
        Map<String, Object> result = new HashMap<>();
        result.put("house", sqlSession.getMapper(HouseMapper.class).selectHouseInfo(maxLat, maxLng, minLat, minLng));
        result.put("cctv", sqlSession.getMapper(HouseMapper.class).selectCctvInfo(maxLat, maxLng, minLat, minLng));
        result.put("corona", sqlSession.getMapper(HouseMapper.class).selectCoronaInfo(maxLat, maxLng, minLat, minLng));
        result.put("school", sqlSession.getMapper(HouseMapper.class).selectSchoolInfo(maxLat, maxLng, minLat, minLng));
        return result;
    }

    @Override
    public List<SearchResultDto> selectSearchList(String gu_code, String dong_code, ArrayList<Integer> type, String name) {
        List<SearchResultDto> list = new ArrayList<>();
        for (int i : type) {
            list.addAll(sqlSession.getMapper(HouseMapper.class).selectSearch(gu_code, dong_code, i, name));
        }
        System.out.println(list);
        return list;
    }
}
