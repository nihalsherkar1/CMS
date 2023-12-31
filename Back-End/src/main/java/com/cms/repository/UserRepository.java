package com.cms.repository;

 

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cms.entities.Users;

@Repository
public interface UserRepository extends JpaRepository<Users, Long> {
	
     Users findByEmail(String email);
     Users findByPassword(String password);
     
     
}
