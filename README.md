# 4Sum (Python) 

## 📌 Problem Description

Given an array `nums` of `n` integers, return **all unique quadruplets**
`[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are **distinct indices**
- The sum of the four values equals `target`:


The result can be returned in **any order**, but **duplicate quadruplets are not allowed**.
(https://thita.ai/problems/four-sum)

This problem is a natural extension of the **2Sum** and **3Sum** problems and tests:
- Sorting
- Two-pointer techniques
- Duplicate handling
- Time-complexity optimization

---

## 🧠 Key Considerations

- The same value may appear multiple times in the array, but each quadruplet must be unique.
- Indices must be distinct, even if values are the same.
- Python’s large integer support safely handles the given value ranges.
- A naive brute-force solution is impractical for larger inputs.

---

## ✨ Examples

### Example 1

**Input**
```python
nums = [1, 0, -1, 0, -2, 2]
target = 0
