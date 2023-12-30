package com.cms.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.cms.entities.Users;
import com.cms.services.UserServiceImpl;

 
@RestController
@RequestMapping("/cms/usercontroller")
public class UserController {

	@Autowired
	private UserServiceImpl serviceImpl;
	
	@PostMapping("/add")
	public ResponseEntity<Users> addUser(  @RequestPart("image") MultipartFile file,
	        @RequestParam("name") String name,
	        @RequestParam("email") String email,
	        @RequestParam("password") String password  ) {
		    
		try {
			 byte[] imageData = file.getBytes();
			 Users user = new Users();
			 user.setName(name);
		        user.setEmail(email);
		        user.setPassword(password);
		        user.setImage(imageData);
		        Users result = serviceImpl.addUser(user);
			 return new ResponseEntity<>(result,HttpStatus.CREATED);
		 
		} catch (Exception e) {
			return new ResponseEntity<Users>(HttpStatus.INTERNAL_SERVER_ERROR);
		}
		
	}
	
	
//	@PostMapping("/login")
//	public ResponseEntity<String>loginUser(@RequestParam("email")String email, @RequestParam("password")String password){
//		try {
//			boolean isValidLogin=serviceImpl.validateLogin(email, password);
//			
//			if(isValidLogin) {
//				return new ResponseEntity<>("Login Successfull",HttpStatus.OK);
//			}else {
//				return new ResponseEntity<>("Invalid email or password", HttpStatus.UNAUTHORIZED);
//			}
//		} catch (Exception e) {
//			return new ResponseEntity<>("Internal Server Error", HttpStatus.INTERNAL_SERVER_ERROR);
//		}
//	}
	@PostMapping("/login")
	public ResponseEntity<String> loginUser(@RequestBody Map<String, String> loginData) {
	    try {
	        String email = loginData.get("email");
	        String password = loginData.get("password");

	        boolean isValidLogin = serviceImpl.validateLogin(email, password);

	        boolean isPassword=serviceImpl.validatePassword(password);
	        
	        if(isPassword==true) {
	        	return new ResponseEntity<>("Password check",HttpStatus.OK);
	        }
	        
	        if (isValidLogin) {
	            return new ResponseEntity<>("Login Successful", HttpStatus.OK);
	        } else {
	            return new ResponseEntity<>("Invalid email or password", HttpStatus.UNAUTHORIZED);
	        }
	    } catch (Exception e) {
	        return new ResponseEntity<>("Internal Server Error", HttpStatus.INTERNAL_SERVER_ERROR);
	    }
	}

}
