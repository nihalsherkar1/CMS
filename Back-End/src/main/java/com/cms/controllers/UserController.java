package com.cms.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.models.User;
import com.cms.services.UserService;

@CrossOrigin("*")
@RestController
@RequestMapping("/cms/user")
public class UserController {
	
	@Autowired
	private UserService userv;
	
	@PostMapping("/register")
	public String addUser(@RequestBody User user) {
		
		return userv.registerUser(user);
	}

}
