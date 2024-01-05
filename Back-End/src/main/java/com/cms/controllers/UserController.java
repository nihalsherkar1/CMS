package com.cms.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.dto.ProfileDto;
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
	
	
	@PostMapping("/getdata")
	public ProfileDto getData(@RequestBody User user) {
		return userv.getData(user);
	}

	@PutMapping("updatename")
	public String updateName(@RequestBody User user) {
		return userv.updateName(user);
	}
	
	@PutMapping("updateemail")
	public String updateEmail(@RequestBody User user) {
		return  userv.UpdateEmail(user);
	}
}
