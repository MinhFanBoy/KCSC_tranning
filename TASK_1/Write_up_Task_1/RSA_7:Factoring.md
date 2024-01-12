
## RSA_7

---

**_TASK_**

Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.

---

```python


from factordb.factordb import FactorDB

def main():
    N = 510143758735509025530880200653196460532653147

    primes = FactorDB(N)
    primes.connect()
    print(min(primes.get_factor_list()))
    

if __name__ == "__main__":
    main()



```


