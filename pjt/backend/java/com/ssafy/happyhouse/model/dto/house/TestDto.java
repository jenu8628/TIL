package com.ssafy.happyhouse.model.dto.house;

public class TestDto {

    private int id;
    private String jibun;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getJibun() {
        return jibun;
    }

    public void setJibun(String jibun) {
        this.jibun = jibun;
    }

    @Override
    public String toString() {
        return "TestDto{" +
                "id=" + id +
                ", jibun='" + jibun + '\'' +
                '}';
    }
}
