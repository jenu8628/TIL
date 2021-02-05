package com.ssafy.happyhouse.model.dto.house;

public class SearchResultDto {

    private int deal_no;            // deal 번호
    private int deal_amount;        // 가격
    private float area;             // 평
    private int floor;              // 층


    private int type;               // 아파트 타입
    private String house_name;      // 아파트 이름
    private String jibun;           // 지번
    private String house_lat;       // 위도
    private String house_lng;       // 경도

    public int getDeal_no() {
        return deal_no;
    }

    public void setDeal_no(int deal_no) {
        this.deal_no = deal_no;
    }

    public int getDeal_amount() {
        return deal_amount;
    }

    public void setDeal_amount(int deal_amount) {
        this.deal_amount = deal_amount;
    }

    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public String getHouse_name() {
        return house_name;
    }

    public void setHouse_name(String house_name) {
        this.house_name = house_name;
    }

    public String getJibun() {
        return jibun;
    }

    public void setJibun(String jibun) {
        this.jibun = jibun;
    }

    public String getHouse_lat() {
        return house_lat;
    }

    public void setHouse_lat(String house_lat) {
        this.house_lat = house_lat;
    }

    public String getHouse_lng() {
        return house_lng;
    }

    public void setHouse_lng(String house_lng) {
        this.house_lng = house_lng;
    }

    @Override
    public String toString() {
        return "SearchResultDto{" +
                "deal_no=" + deal_no +
                ", deal_amount=" + deal_amount +
                ", area=" + area +
                ", floor=" + floor +
                ", type=" + type +
                ", house_name='" + house_name + '\'' +
                ", jibun='" + jibun + '\'' +
                ", house_lat='" + house_lat + '\'' +
                ", house_lng='" + house_lng + '\'' +
                '}';
    }
}
