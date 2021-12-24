package com.travelrecommendation.travel.service;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.travelrecommendation.travel.dto.UserFinalRequest;
import com.travelrecommendation.travel.dto.UserFinalResponse;
import lombok.extern.slf4j.Slf4j;
import org.apache.catalina.User;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

@Slf4j
@Service
public class ModelRequest {
    public UserFinalResponse startModel(UserFinalRequest request) throws IOException, InterruptedException {

//        String command ="pwd";//"python3 /Users/jihoonan/Desktop/travelRecommendation/backend/test.py";
//        위에 command는 예시임.
        // 이 부분 이제 아님. flask랑 통신함.

        String url = "http://52.78.2.120:8081/";
        String sb = "";
        Gson gson = new Gson();

        HttpClient client = HttpClientBuilder.create().build();

        HttpPost httpPost = new HttpPost(url);
        try {
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Connection", "keep-alive");
            httpPost.setHeader("Content-type", "application/json");

            httpPost.setEntity(new StringEntity(gson.toJson(request)));

            HttpResponse response = client.execute(httpPost);

            if (response.getStatusLine().getStatusCode() == 200) {
                String result = EntityUtils.toString(response.getEntity());
                JsonParser parser = new JsonParser();
                JsonObject jsonObject=(JsonObject)parser.parse(result);

                UserFinalResponse answer = new UserFinalResponse();
                answer.setType(Integer.getInteger(jsonObject.get("type").getAsString()));
                System.out.println(answer.getType());

                ArrayList<String> places = new ArrayList<>();
                places.add(jsonObject.get("first").getAsString());
                places.add(jsonObject.get("second").getAsString());
                places.add(jsonObject.get("third").getAsString());

                ArrayList<String> alchol = new ArrayList<>();
                alchol.add(jsonObject.get("alchol1").getAsString());
                alchol.add(jsonObject.get("alchol2").getAsString());
                alchol.add(jsonObject.get("alchol3").getAsString());

                ArrayList<String> restaurant = new ArrayList<>();
                restaurant.add(jsonObject.get("restaurant1").getAsString());
                restaurant.add(jsonObject.get("restaurant2").getAsString());
                restaurant.add(jsonObject.get("restaurant3").getAsString());

                HashMap<String,List<String>> token = new HashMap<>();
                token.put("places",places);
                token.put("alchol",alchol);
                token.put("restaurant",restaurant);

                answer.setResult(token);


                return answer;

            } else {
                throw new IllegalAccessException("Status of model is not 200");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }


//        List<String> cmd= new ArrayList<>();
//        cmd.add("python3");
//        cmd.add("/Users/jihoonan/Desktop/travelRecommendation/backend/test.py");
//        cmd.add(request.getType());
//        ProcessBuilder builder=new ProcessBuilder(cmd);
//        Process process=builder.start();
//        InputStream input =process.getInputStream();
//
//        int exitVal= process.waitFor();
//        String text = new BufferedReader(
//                new InputStreamReader(input, StandardCharsets.UTF_8))
//                .lines()
//                .collect(Collectors.joining("\n"));
//        String []str=text.split(" ");
//        ArrayList<String> tokens=new ArrayList<>();
//        for (int i=0; i<str.length; i++){
//            tokens.add(str[i]);
//        }
//
//        return tokens;
        UserFinalResponse answer2 = new UserFinalResponse();
        answer2.setType(1);
        return answer2;
    }
}