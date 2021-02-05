package com.ssafy.happyhouse.model.dto;

public class NoticeDto {

    private int notice_num;
    private String notice_writer;
    private String notice_title;
    private String notice_content;
    private int notice_cnt;
    private String write_date;

    public int getNotice_num() {
        return notice_num;
    }

    public void setNotice_num(int notice_num) {
        this.notice_num = notice_num;
    }

    public String getNotice_writer() {
        return notice_writer;
    }

    public void setNotice_writer(String notice_writer) {
        this.notice_writer = notice_writer;
    }

    public String getNotice_title() {
        return notice_title;
    }

    public void setNotice_title(String notice_title) {
        this.notice_title = notice_title;
    }

    public String getNotice_content() {
        return notice_content;
    }

    public void setNotice_content(String notice_content) {
        this.notice_content = notice_content;
    }

    public int getNotice_cnt() {
        return notice_cnt;
    }

    public void setNotice_cnt(int notice_cnt) {
        this.notice_cnt = notice_cnt;
    }

    public String getWrite_date() {
        return write_date;
    }

    public void setWrite_date(String write_date) {
        this.write_date = write_date;
    }

    @Override
    public String toString() {
        return "NoticeDto{" +
                "notice_num=" + notice_num +
                ", notice_writer='" + notice_writer + '\'' +
                ", notice_title='" + notice_title + '\'' +
                ", notice_content='" + notice_content + '\'' +
                ", notice_cnt=" + notice_cnt +
                ", write_date='" + write_date + '\'' +
                '}';
    }
}
