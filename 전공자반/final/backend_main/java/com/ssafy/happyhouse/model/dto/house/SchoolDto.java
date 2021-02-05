package com.ssafy.happyhouse.model.dto.house;

public class SchoolDto {

    private String school_id;
    private String school_name;
    private String school_grade;
    private String school_jibun;
    private String lat;
    private String lng;

    public String getSchool_id() {
        return school_id;
    }

    public void setSchool_id(String school_id) {
        this.school_id = school_id;
    }

    public String getSchool_name() {
        return school_name;
    }

    public void setSchool_name(String school_name) {
        this.school_name = school_name;
    }

    public String getSchool_grade() {
        return school_grade;
    }

    public void setSchool_grade(String school_grade) {
        this.school_grade = school_grade;
    }

    public String getSchool_jibun() {
        return school_jibun;
    }

    public void setSchool_jibun(String school_jibun) {
        this.school_jibun = school_jibun;
    }

    public String getLat() {
        return lat;
    }

    public void setLat(String lat) {
        this.lat = lat;
    }

    public String getLng() {
        return lng;
    }

    public void setLng(String lng) {
        this.lng = lng;
    }

    @Override
    public String toString() {
        return "SchoolDto{" +
                "school_id=s'" + school_id + '\'' +
                ", school_name='" + school_name + '\'' +
                ", school_grade='" + school_grade + '\'' +
                ", school_jibun='" + school_jibun + '\'' +
                ", lat='" + lat + '\'' +
                ", lng='" + lng + '\'' +
                '}';
    }
}
