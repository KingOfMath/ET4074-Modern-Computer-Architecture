#!/bin/bash
#Backup
mv ./configuration.mm ./configuration_backup.mm
#Counter used in the loops
counter=1

#====1	Range for Issuewidth====
for i in {8..8}
do
	sed -e "s/RES: IssueWidth     4/RES: IssueWidth     $i/; s/RES: IssueWidth.0   4/RES: IssueWidth.0   $i/" ./configuration_backup.mm > temp_test1.txt

#====2	Range for RES: MemLoad====
	j = 8
		sed -e "s/RES: MemLoad        1/RES: MemLoad        8/" ./temp_test1.txt > temp_test2.txt

#====3 	Range for RES: MemStore====
		k = 1
			sed -e "s/RES: MemStore       1/RES: MemStore       1/" ./temp_test2.txt > temp_test3.txt
			
#====4	Range for RES: MemPit====
			l = 1
				sed -e "s/RES: MemPft         1/RES: MemPft         1/" ./temp_test3.txt > temp_test4.txt
				
#====5	Range for RES: ALU.0====
				for m in {8..8}
				do
					sed -e "s/RES: Alu.0          4/RES: Alu.0          $m/" ./temp_test4.txt > temp_test5.txt
					
#====6 	Range for RES: Mpy.0====
					for n in {3..3}
					do
						sed -e "s/RES: Mpy.0          2/RES: Mpy.0          $n/" ./temp_test5.txt > temp_test6.txt
						
#====7 	Range for RES: Memory====
						for o in {8..8}
						do
							sed -e "s/RES: Memory.0       1/RES: Memory.0       $o/" ./temp_test6.txt > temp_test7.txt

#====8	Range for REG:$r0====
							for p in {32..32}
							do
								sed -e 's/REG: $r0            64/REG: $r0            '"$p"'/' ./temp_test7.txt > temp_test8.txt

#====9	Range for REG:$b0====
								for q in {8..8}
								do
								
#=====================================Innermost region of these nested loops==========================================
									mkdir test$counter
									
									#Configuration files genration
									sed -e 's/REG: $b0            8/REG: $b0            '"$q"'/' ./temp_test8.txt > test.mm
									mv ./test.mm ./test$counter
									#Run the benchmark profile
									sed -e 's/REG: $b0            8/REG: $b0            '"$q"'/' ./temp_test8.txt > ./configuration.mm
									
									#Convolution benchmark
									run convolution_3x3 -O3
									
									cd  ./output-convolution_3x3.c
									gprof a.out gmon-nocache.out > convolution_gmon-nocache.txt
									pcntl convolution_3x3.s > convolution_pcntl.txt
									mv ta.log.* convolution_ta_log
									cd ..
									mv ./output-convolution_3x3.c/convolution_gmon-nocache.txt ./test$counter
									mv ./output-convolution_3x3.c/convolution_pcntl.txt ./test$counter
									mv ./output-convolution_3x3.c/convolution_ta_log ./test$counter
									
									
									#Engine benchmark
									run engine -O3
									cd ./output-engine.c
									gprof a.out gmon-nocache.out > engine_gmon-nocache.txt
									pcntl engine.s > engine_pcntl.txt
									mv ta.log.* engine_ta_log
									cd ..
									mv ./output-engine.c/engine_pcntl.txt ./test$counter
									mv ./output-engine.c/engine_gmon-nocache.txt ./test$counter
									mv ./output-engine.c/engine_ta_log ./test$counter
									
									let "counter=counter+1"
#=====================================================================================================================
								
								done
								rm ./temp_test8.txt
							done
							rm ./temp_test7.txt
						done
						rm ./temp_test6.txt
					done
					rm ./temp_test5.txt
				done
				rm ./temp_test4.txt
			rm ./temp_test3.txt
		rm ./temp_test2.txt
	rm ./temp_test1.txt
done 

rm ./configuration.mm
mv ./configuration_backup.mm ./configuration.mm
