from django.contrib.auth.base_user import BaseUserManager




class UserManager(BaseUserManager):
	def _create_user(self, name, email, password, regdno, department, **extras,):
		user = self.create(
			name = name,
			email = self.normalize_email(email),
			regdno = regdno,
			department = Department.objects.get(department)
			)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", False)
		extras.setdefault("is_hod", False)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", False)
		extras.setdefault("is_superuser", False)

		return self._create_user(name, email, password, regdno, department, **extras)

	def create_hod(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", False)
		extras.setdefault("is_superuser", False)


		if extras.get('is_staff') is False:
			raise ValueError("HOD must have staff previliges.")
		return self._create_user(name, email, password, regdno, department, **extras)

	def create_admin(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", True)
		extras.setdefault("is_superuser", False)


		if extras.get('is_staff') is False:
			raise ValueError("Admin must have staff previliges.")
		
		return self._create_user(name, email, password, regdno, department, **extras)

	def create_superuser(self, name, email, password, regdno, department, **extras):
		extras.setdefault("is_staff", True)
		extras.setdefault("is_hod", True)
		extras.setdefault("is_active", False)
		extras.setdefault("is_admin", True)
		extras.setdefault("is_superuser", True)


		if extras.get('is_staff') is False:
			raise ValueError("Super User must have all previliges.")
		
		return self._create_user(name, email, password, regdno, department, **extras)
