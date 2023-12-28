package com.cms.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cms.entities.Users;
import com.cms.repository.UserRepository;

@Service
public class UserServiceImpl implements UserServices {
	
	@Autowired
	private UserRepository userRepository;

	@Override
	public Users addUser(Users user) {
		 
		return userRepository.save(user);
	}

	
}
