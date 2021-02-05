package com.ssafy.happyhouse.model.dto.house;

public class DongDto {
    private String dong_code;
    private String dong_name;

    public String getDong_code() {
        return dong_code;
    }

    public void setDong_code(String dong_code) {
        this.dong_code = dong_code;
    }

    public String getDong_name() {
        return dong_name;
    }

    public void setDong_name(String dong_name) {
        this.dong_name = dong_name;
    }

    @Override
    public String toString() {
        return "DongDto{" +
                "dong_code='" + dong_code + '\'' +
                ", dong_name='" + dong_name + '\'' +
                '}';
    }
}
