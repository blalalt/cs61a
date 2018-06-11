(define (find s predicate)
  'YOUR-CODE-HERE
  (cond
    ((null? s) #f)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  'YOUR-CODE-HERE
  (cond
    ((null? s) nil)
    (else (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)))
  )
)
;scm> (define s (cons-stream 1 (cons-stream 2 nil)))
;scm> (define cycle (cons-stream 1 (cons-stream 1 cycle)))
;scm> (define cycle-within (cons-stream 1 (cons-stream 2 cycle)))
(define (has-cycle s)
  'YOUR-CODE-HERE
  ; fast and slow pointer
    (if (null? s) #f
        (begin
            (define (func slow fast)
                (cond
                    ((null? fast) #f)
                    ((eq? '() (cdr-stream fast)) #f)
                    ((or (eq? (cdr-stream fast) slow) (eq? fast slow)) #t)
                    (else (func (cdr-stream slow) (cdr-stream (cdr-stream fast))))
                )
            )
            (func s (cdr-stream s))
        )
    )
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
  (if (null? s) #f
        (begin
            (define (func slow fast)
                (cond
                    ((null? fast) #f)
                    ((eq? '() (cdr-stream fast)) #f)
                    ((or (eq? (cdr-stream fast) slow) (eq? fast slow)) #t)
                    (else (func (cdr-stream slow) (cdr-stream (cdr-stream fast))))
                )
            )
            (func s (cdr-stream s))
        )
    )
)
