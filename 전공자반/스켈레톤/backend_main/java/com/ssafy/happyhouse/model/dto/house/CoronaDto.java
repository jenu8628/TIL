package com.ssafy.happyhouse.model.dto.house;

public class CoronaDto {

    private int clinic_no;
    private String clinic_name;
    private String weekday_time;
    private String saturday_time;
    private String sunday_time;
    private String phone_number;
    private String clinic_lat;
    private String clinic_lng;

    public String getClinic_lat() {
        return clinic_lat;
    }

    public void setClinic_lat(String clinic_lat) {
        this.clinic_lat = clinic_lat;
    }

    public String getClinic_lng() {
        return clinic_lng;
    }

    public void setClinic_lng(String clinic_lng) {
        this.clinic_lng = clinic_lng;
    }

    public int getClinic_no() {
        return clinic_no;
    }

    public void setClinic_no(int clinic_no) {
        this.clinic_no = clinic_no;
    }

    public String getClinic_name() {
        return clinic_name;
    }

    public void setClinic_name(String clinic_name) {
        this.clinic_name = clinic_name;
    }

    public String getWeekday_time() {
        return weekday_time;
    }

    public void setWeekday_time(String weekday_time) {
        this.weekday_time = weekday_time;
    }

    public String getSaturday_time() {
        return saturday_time;
    }

    public void setSaturday_time(String saturday_time) {
        this.saturday_time = saturday_time;
    }

    public String getSunday_time() {
        return sunday_time;
    }

    public void setSunday_time(String sunday_time) {
        this.sunday_time = sunday_time;
    }

    public String getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(String phone_number) {
        this.phone_number = phone_number;
    }

    @Override
    public String toString() {
        return "CoronaDto{" +
                "clinic_no=" + clinic_no +
                ", clinic_name='" + clinic_name + '\'' +
                ", weekday_time='" + weekday_time + '\'' +
                ", saturday_time='" + saturday_time + '\'' +
                ", sunday_time='" + sunday_time + '\'' +
                ", phone_number='" + phone_number + '\'' +
                ", clinic_lat='" + clinic_lat + '\'' +
                ", clinic_lng='" + clinic_lng + '\'' +
                '}';
    }
}
