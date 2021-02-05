package com.ssafy.happyhouse.service;

import com.ssafy.happyhouse.model.dto.house.DongDto;
import com.ssafy.happyhouse.model.dto.house.GuDto;
import com.ssafy.happyhouse.model.dto.house.SearchResultDto;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public interface HouseService {

    // 구 정보 불러오기
    public List<GuDto> selectGuList();

    // 동 정보 불러오기
    public List<DongDto> selectDongList(String gu);

    // 좌표 위치에 따른 자동 데이터 전송
    public Map<String, Object> selectLatLng(double maxLat, double maxLng, double minLat, double minLng);

    // 검색 결과 찾기
    public List<SearchResultDto> selectSearchList(String gu_code, String dong_code, ArrayList<Integer> type, String name);
}
