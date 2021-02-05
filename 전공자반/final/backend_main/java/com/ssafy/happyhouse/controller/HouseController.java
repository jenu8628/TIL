package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.house.DongDto;
import com.ssafy.happyhouse.model.dto.house.GuDto;
import com.ssafy.happyhouse.model.dto.house.SearchResultDto;
import com.ssafy.happyhouse.service.HouseService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/house")
public class HouseController {

    @Autowired
    private HouseService houseService;

    public static final Logger logger = LoggerFactory.getLogger(HouseController.class);
    public static final String SUCCESS = "success";
    public static final String FAIL = "fail";

    @GetMapping(value = "gu", produces = "application/json; charset=utf8")
    public ResponseEntity<List<GuDto>> getGuList() {
        List<GuDto> guList = houseService.selectGuList();
        logger.info("구 리스트 요청");
        return new ResponseEntity<>(guList, HttpStatus.OK);
    }

    @GetMapping(value = "dong", produces = "application/json; charset=utf8")
    public ResponseEntity<List<DongDto>> getDongList(@RequestParam(value = "gu") String gu) {
        List<DongDto> dongList = houseService.selectDongList(gu);
        logger.info("동 리스트 요청 : {}", gu);
        return new ResponseEntity<>(dongList, HttpStatus.OK);
    }

    @PostMapping(value = "latlng", produces = "application/json; charset=utf8")
    public ResponseEntity<Map<String, Object>> postLatLng(@RequestBody Map<String, String> map) {
        logger.info("화면 검색 결과 요청");
        double maxLat = Double.parseDouble(map.get("maxlat"));
        double minLat = Double.parseDouble(map.get("minlat"));
        double maxLng = Double.parseDouble(map.get("maxlng"));
        double minLng = Double.parseDouble(map.get("minlng"));

        return new ResponseEntity<>(houseService.selectLatLng(maxLat,  maxLng, minLat, minLng), HttpStatus.OK);
    }

    @PostMapping(value = "/search", produces = "application/json; charset=utf8")
    public ResponseEntity<List<SearchResultDto>> getAptList(@RequestBody Map<String, Object> map) {
        List<SearchResultDto> aptList = houseService.selectSearchList((String) map.get("gu"),
                (String) map.get("dong"), (ArrayList<Integer>)map.get("type"), (String) map.get("name"));
        logger.info("아파트 검색 결과 요청");
        System.out.println(aptList);
        return new ResponseEntity<>(aptList, HttpStatus.OK);
    }
}
