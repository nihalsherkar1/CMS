package com.cms.services;

import java.util.List;
import java.util.Optional;

import com.cms.entities.Users;

public interface UserServices {

	// Save User
	public Users addUser(Users user);
	
	//Read 
	List<Users>fetchUsers();
	
	 public Optional<Users>  getUserById(Long id);
	
	//Update
	Users updateUser(Users users, Long id);
	
	//Delete
	public void deleteUserById(Long id);
	
	
	
}
