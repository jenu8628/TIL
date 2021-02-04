package com.ssafy.happyhouse.model.mapper;

import com.ssafy.happyhouse.model.dto.house.*;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface HouseMapper {

    // 구 불러오기
    public List<GuDto> selectGuList();

    // 동 불러오기
    public List<DongDto> selectDongList(String gu_code);


    // 아파트 정보 가저오기
    public List<SearchResultDto> selectHouseInfo(double maxLat, double maxLng, double minLat, double minLng);

    // 버스 정류장 갖고오기
    public List<LatLngDto> selectBusInfo(double maxLat, double maxLng, double minLat, double minLng);

    // CCTV 갖고오기
    public List<LatLngDto> selectCctvInfo(double maxLat, double maxLng, double minLat, double minLng);

    // 코로나 진료소 갖고오기
    public List<CoronaDto> selectCoronaInfo(double maxLat, double maxLng, double minLat, double minLng);

    // 학교 정보 갖고오기
    public List<SchoolDto> selectSchoolInfo(double maxLat, double maxLng, double minLat, double minLng);

    // 지하철 갖고오기
    public List<LatLngDto> selectSubwayInfo(double maxLat, double maxLng, double minLat, double minLng);

    // 아파트 검색하기
    public List<SearchResultDto> selectSearch(String gu_code, String dong_code, int type, String name);




    // 데이터 정리용
    public List<TestDto> selectTest1();
    public List<TestDto> selectTest2();
    public void updateTest1(int clinic_no, String clinic_lat, String clinic_lng);
    public void updateTest2(int subway_no, String subway_lat, String subway_lng);
}
