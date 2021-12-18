package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserFinalRequest {
    private String type;
    private int starting;
    private int destination;
    private int mvp;
}
