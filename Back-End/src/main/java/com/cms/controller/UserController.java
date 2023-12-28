package com.cms.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.entities.Users;
import com.cms.services.UserServiceImpl;

@RestController
@RequestMapping("/cms/usercontroller")
public class UserController {

	@Autowired
	private UserServiceImpl serviceImpl;
	
	@PostMapping("/add")
	public ResponseEntity<Users> addUser( @RequestBody  Users user) {
		    
		try {
			Users result= serviceImpl.addUser(user);
			
			 return new ResponseEntity<>(result,HttpStatus.CREATED);
		 
		} catch (Exception e) {
			return new ResponseEntity<Users>(HttpStatus.INTERNAL_SERVER_ERROR);
		}
		
	}
}
