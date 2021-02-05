package com.ssafy.happyhouse.model.dto;

public class MemberDto {

    private String user_id;
    private String user_password;
    private String user_email;
    private int user_info;

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }

    public String getUser_password() {
        return user_password;
    }

    public void setUser_password(String user_password) {
        this.user_password = user_password;
    }

    public String getUser_email() {
        return user_email;
    }

    public void setUser_email(String user_email) {
        this.user_email = user_email;
    }

    public int getUser_info() {
        return user_info;
    }

    public void setUser_info(int user_info) {
        this.user_info = user_info;
    }

    @Override
    public String toString() {
        return "MemberDto{" +
                "user_id='" + user_id + '\'' +
                ", user_password='" + user_password + '\'' +
                ", user_email='" + user_email + '\'' +
                ", user_info=" + user_info +
                '}';
    }
}
