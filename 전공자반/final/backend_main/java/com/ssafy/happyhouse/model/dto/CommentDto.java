package com.ssafy.happyhouse.model.dto;

public class CommentDto {
    private int comment_num;
    private int board_num;
    private String comment_writer;
    private String comment_content;
    private String write_date;

    public int getComment_num() {
        return comment_num;
    }

    public void setComment_num(int comment_num) {
        this.comment_num = comment_num;
    }

    public int getBoard_num() {
        return board_num;
    }

    public void setBoard_num(int board_num) {
        this.board_num = board_num;
    }

    public String getComment_writer() {
        return comment_writer;
    }

    public void setComment_writer(String comment_writer) {
        this.comment_writer = comment_writer;
    }

    public String getComment_content() {
        return comment_content;
    }

    public void setComment_content(String comment_content) {
        this.comment_content = comment_content;
    }

    public String getWrite_date() {
        return write_date;
    }

    public void setWrite_date(String write_date) {
        this.write_date = write_date;
    }

    @Override
    public String toString() {
        return "CommentDto{" +
                "comment_num=" + comment_num +
                ", board_num=" + board_num +
                ", comment_writer='" + comment_writer + '\'' +
                ", comment_content='" + comment_content + '\'' +
                ", write_date='" + write_date + '\'' +
                '}';
    }
}
