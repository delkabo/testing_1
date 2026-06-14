#change_hat(Hats.Gray_Hat)
#while True:
print(get_pos_x())
print(get_pos_x())
bush_less_carriot=2
hay_less_carriot=2
all_plants = [Entities.Bush, Entities.Carrot, Entities.Grass, Entities.Tree]
while True:
	if get_pos_x() != 0:
		move(East)
	else:
		print("верное направление x =",get_pos_x())
		#print(get_pos_x())
		break
while True:
	if get_pos_y() != 0:
		move(North)
	else:
		print("верное направление y =",get_pos_y())
		#print(get_pos_y())
		break
		#print(get_pos_x())
		#print(get_pos_x())
	#elif get_pos_x() == 0 and get_pos_y() == 0:
		#break
		#if get_pos_x() == 0 or get_pos_y() == 0:
		#	break
water_count=35
water_x = 0
while True:
	for x in range(get_world_size()):
		num_trees = num_items(Items.Wood)
		#print(num_trees)
		if num_trees == 900:
			break
		#harvest()
		#plant(Entities.Carrot)
		for i in range(get_world_size()):
			#print(get_entity_type())
			#till()
			#plant(Entities.Carrot)
			#print(get_world_size())
			#if get_entity_type() == Entities.Grass:
			carriot_hay_dev = num_items(Items.Carrot) // num_items(Items.Hay)
			if can_harvest():
				harvest()
			#	plant(Entities.Bush)
				#print(get_entity_type())
			#if get_ground_type() == Grounds.Grassland:
				till()
				carriot_wood_dev = num_items(Items.Carrot) // num_items(Items.Wood)
				#print(carriot_wood_dev, "-")
				if carriot_wood_dev > bush_less_carriot:
					while get_ground_type() != Grounds.Grassland:
						till()
				if get_ground_type() == Grounds.Grassland:
					if carriot_hay_dev < hay_less_carriot:
						plant(Entities.Bush)
					# Поливка воды
					#if water_count == 0:
					#	water_x = 0 
					if num_items(Items.Water) > water_count and water_x == 0:
						# if water_x == 0:
						water_count = 0
						use_item(Items.Water)
						if num_items(Items.Water) == 0:
							water_x = 1
					if num_items(Items.Water) > 35:
						water_count = 35
						water_x = 0
						
				else:
					plant(Entities.Carrot)
				#use_item(Items.Water)
				move(North)
			else:
				if carriot_hay_dev > hay_less_carriot:
					till()
				elif get_entity_type() == None and get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)
				move(North)
		move(East)
				#z = 0
			#for plants_x in all_plants:
				#z = z + 1
			#	if get_entity_type() != plants_x:
					#and len(all_plants) == z
			#		if get_ground_type() == Grounds.Grassland:
			#			plant(Entities.Carrot)
			#		else:
			#			plant(Entities.Bush)
			#else:
				#use_item(Items.Water)
	
