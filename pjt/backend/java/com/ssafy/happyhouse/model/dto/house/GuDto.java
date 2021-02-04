package com.ssafy.happyhouse.model.dto.house;

public class GuDto {

    private String gu_code;
    private String gu_name;

    public String getGu_code() {
        return gu_code;
    }

    public void setGu_code(String gu_code) {
        this.gu_code = gu_code;
    }

    public String getGu_name() {
        return gu_name;
    }

    public void setGu_name(String gu_name) {
        this.gu_name = gu_name;
    }

    @Override
    public String toString() {
        return "GuCodeDto{" +
                "gu_code='" + gu_code + '\'' +
                ", gu_name='" + gu_name + '\'' +
                '}';
    }
}
