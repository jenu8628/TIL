package com.ssafy.happyhouse.controller;

import com.ssafy.happyhouse.model.dto.house.TestDto;
import com.ssafy.happyhouse.service.TestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/test")
public class TestController {

    @Autowired
    private TestService testService;

    @GetMapping(value = "/corona", produces = "application/json; charset=utf8")
    public ResponseEntity<List<TestDto>> getCorona() {
        return new ResponseEntity<>(testService.selectCorona(), HttpStatus.OK);
    }

    @PostMapping(value = "/corona")
    public void postCorona(@RequestBody Map<String, String> map) {
        int id = Integer.parseInt(map.get("id"));
        String lat = map.get("lat");
        String lng = map.get("lng");
        testService.updateCorona(id, lat, lng);
    }

    @GetMapping(value = "/subway", produces = "application/json; charset=utf8")
    public ResponseEntity<List<TestDto>> getSubway() {
        return new ResponseEntity<>(testService.selectSubway(), HttpStatus.OK);
    }

    @PostMapping(value = "/subway")
    public void postSubway(@RequestBody Map<String, String> map) {
        int id = Integer.parseInt(map.get("id"));
        String lat = map.get("lat");
        String lng = map.get("lng");
        testService.updateSubway(id, lat, lng);
    }
}
