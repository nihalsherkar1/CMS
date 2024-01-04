package com.cms.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cms.dto.LogIDto;
import com.cms.services.LogInService;

@CrossOrigin("*")
@RestController
@RequestMapping("/cms/auth")
public class AuthController {
	
	@Autowired
	private LogInService lser;

	@PostMapping("/login")
	public String login(@RequestBody LogIDto cred) {
		return lser.validateEmail(cred.getEmail());
	}
}
