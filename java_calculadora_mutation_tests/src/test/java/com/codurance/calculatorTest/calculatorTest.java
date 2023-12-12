package com.codurance.calculatorTest;

import com.codurance.calculator.calculator;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
public class calculatorTest {

        private calculator c;

        @BeforeEach
        public void setup () {
            c = new calculator();
        }

        @Test
        public void testBasicAdd() {
            Assertions.assertEquals(c.add(1,1),2);
        }

        @Test
        public void testSubtract() {
            Assertions.assertEquals(c.subtract(3,2),1);
        }

        @Test
        public void testMultiply(){
            Assertions.assertEquals(c.multiply(2,6),12);
        }

        @Test
        public void testDiv(){
            Assertions.assertEquals(c.divide(0,100),0);
            Assertions.assertEquals(c.divide(105,10),10);
        }
        @Test
        public void testSummation(){
            Assertions.assertEquals(3, c.summation(2));
            Assertions.assertEquals(1, c.summation(1));
            Assertions.assertEquals(0, c.summation(0));
        }
        @Test
        public void testPositive(){
            Assertions.assertTrue(c.isPositive(2));
            Assertions.assertFalse(c.isPositive(-2));
            Assertions.assertFalse(c.isPositive(0));
        }

        @Test
        public void testCompare(){
            Assertions.assertEquals(0, c.compare(0, 0));
            Assertions.assertEquals(1, c.compare(2, 0));
            Assertions.assertEquals(-1, c.compare(2,5));
        }
    }

