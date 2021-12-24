package com.travelrecommendation.travel.dto;


import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.List;

@Getter
@Setter
public class UserTypeResultRequest {

    private List<HashMap<String,Double>> answer;

}
