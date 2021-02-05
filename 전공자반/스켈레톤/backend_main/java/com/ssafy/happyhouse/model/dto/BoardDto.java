package com.ssafy.happyhouse.model.dto;

public class BoardDto {

    private int board_num;
    private String board_writer;
    private String board_title;
    private String board_content;
    private int board_cnt;
    private String write_date;
    private int comment_cnt;

    public int getBoard_num() {
        return board_num;
    }

    public void setBoard_num(int board_num) {
        this.board_num = board_num;
    }

    public String getBoard_writer() {
        return board_writer;
    }

    public void setBoard_writer(String board_writer) {
        this.board_writer = board_writer;
    }

    public String getBoard_title() {
        return board_title;
    }

    public void setBoard_title(String board_title) {
        this.board_title = board_title;
    }

    public String getBoard_content() {
        return board_content;
    }

    public void setBoard_content(String board_content) {
        this.board_content = board_content;
    }

    public int getBoard_cnt() {
        return board_cnt;
    }

    public void setBoard_cnt(int board_cnt) {
        this.board_cnt = board_cnt;
    }

    public String getWrite_date() {
        return write_date;
    }

    public void setWrite_date(String write_date) {
        this.write_date = write_date;
    }

    public int getComment_cnt() {
        return comment_cnt;
    }

    public void setComment_cnt(int comment_cnt) {
        this.comment_cnt = comment_cnt;
    }

    @Override
    public String toString() {
        return "BoardDto{" +
                "board_num=" + board_num +
                ", board_writer='" + board_writer + '\'' +
                ", board_title='" + board_title + '\'' +
                ", board_content='" + board_content + '\'' +
                ", board_cnt=" + board_cnt +
                ", write_date='" + write_date + '\'' +
                ", comment_cnt=" + comment_cnt +
                '}';
    }
}
