package com.ssafy.happyhouse.model.dto;

import java.util.List;

public class PageDto {

    private List<?> List;
    private int curPage;
    private int startPage;
    private int endPage;
    private int totalPage;

    public PageDto() {}

    public PageDto(java.util.List<?> list, int curPage, int startPage, int endPage, int totalPage) {
        List = list;
        this.curPage = curPage;
        this.startPage = startPage;
        this.endPage = endPage;
        this.totalPage = totalPage;
    }

    public java.util.List<?> getList() {
        return List;
    }

    public void setList(java.util.List<?> list) {
        List = list;
    }

    public int getCurPage() {
        return curPage;
    }

    public void setCurPage(int curPage) {
        this.curPage = curPage;
    }

    public int getStartPage() {
        return startPage;
    }

    public void setStartPage(int startPage) {
        this.startPage = startPage;
    }

    public int getEndPage() {
        return endPage;
    }

    public void setEndPage(int endPage) {
        this.endPage = endPage;
    }

    public int getTotalPage() {
        return totalPage;
    }

    public void setTotalPage(int totalPage) {
        this.totalPage = totalPage;
    }

    @Override
    public String toString() {
        return "PageDto{" +
                "List=" + List +
                ", curPage=" + curPage +
                ", startPage=" + startPage +
                ", endPage=" + endPage +
                ", totalPage=" + totalPage +
                '}';
    }
}
